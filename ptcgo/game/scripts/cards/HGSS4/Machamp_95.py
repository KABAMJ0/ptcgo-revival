from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _fighting_tag_ready(board, player_id, pokemon) -> bool:
    return not is_in_active_spot(pokemon)


async def _fighting_tag(ctx):
    champ = ctx.attacker
    active = ctx.my_active()
    if active is None or active is champ:
        return
    moved = [e for e in ctx.attached_energies(active)
             if PokemonTypes.FIGHTING.value in (e.get_attribute(AttrID.POKEMON_TYPES) or [])]
    for energy in list(moved):
        await ctx.move_energy(energy, champ)
    await ctx.switch_active(ctx.player_id, champ)


def _damaged_bench(ctx) -> int:
    return sum(1 for p in ctx.my_bench()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p))

card = PokemonCardDef(
    guid="278a4f09-6b6a-50d3-837a-6677b605c617",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Prime", "Machamp"],
    subtypes=["Stage 2", "Prime"],
    collector_number=95,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Fighting Tag",
            game_text="Once during your turn (before your attack), if Machamp is on your Bench, you may move all Fighting Energy attached to your Active Pok\u00e9mon to Machamp. If you do, switch Machamp with your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_fighting_tag_ready,
            effect=_fighting_tag,
        ),
        Attack(
            title="Crushing Punch",
            game_text="Discard a Special Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Champ Buster",
            game_text="Does 100 damage plus 10 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=damage_per(_damaged_bench, 10, base=100),
        ),
    ],
)
