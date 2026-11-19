from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_lightning(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _voltage_increase(ctx):
    me = ctx.attacker
    holders = [p for p in ctx.my_pokemon_in_play()
               if p.entity_id != me.entity_id
               and any(_is_lightning(e) for e in ctx.attached_energies(p))]
    if not holders:
        return
    source = holders[0] if len(holders) == 1 else await ctx.choose_pokemon(
        holders, "Choose a Pok\u00e9mon to move a Lightning Energy from")
    if source is None:
        return
    lightning = [e for e in ctx.attached_energies(source) if _is_lightning(e)]
    pick = lightning[0] if len(lightning) == 1 else (
        await ctx.choose_cards(lightning, 1, prompt="Choose a Lightning Energy to move") or [])
    if pick:
        await ctx.move_energy(pick[0], me)

card = PokemonCardDef(
    guid="2563949e-43b4-5b5f-8e9b-65c381a81e00",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Prime", "Raichu"],
    subtypes=["Stage 1", "Prime"],
    collector_number=83,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Voltage Increase",
            game_text="As often as you like during your turn (before your attack), you may move a Lightning Energy attached to 1 of your Pok\u00e9mon to Raichu. This power can't be used if Raichu is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=unafflicted,
            effect=_voltage_increase,
        ),
        Attack(
            title="Mega Thunderbolt",
            game_text="Discard all Energy attached to Raichu.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
