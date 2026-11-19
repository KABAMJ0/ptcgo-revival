from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

def _is_fire(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def _lava_flow(ctx):
    fire = [e for e in ctx.attached_energies(ctx.attacker) if _is_fire(e)]
    picks = []
    if fire:
        picks = await ctx.choose_cards(
            fire, len(fire), minimum=0,
            prompt="Choose any number of Fire Energy to discard")
    if picks:
        await ctx.discard_cards(list(picks))
    await ctx.deal_damage(60 + 20 * len(picks))

card = PokemonCardDef(
    guid="48b90675-78b2-502c-a927-a7388df03590",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="HGSS3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Lava Flow",
            game_text="You may discard any number of Fire Energy cards attached to Magcargo. If you do , this attack does 60 damage plus 20 more damage for each Fire Energy card you discarded.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=_lava_flow,
        ),
    ],
)
