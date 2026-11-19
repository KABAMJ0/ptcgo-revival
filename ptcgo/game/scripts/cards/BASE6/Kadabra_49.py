from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_is_psychic_energy = basic_energy_of("psychic")


def _can_recover(board, player_id, pokemon):
    """The attack needs a Psychic Energy on Kadabra to pay its discard cost."""
    active = board.active_pokemon(player_id)
    return active is not None \
        and any(_is_psychic_energy(card) for card in board.attached_energies(active))


async def recover(ctx):
    """Discard a Psychic Energy from Kadabra, then remove all its damage."""
    attacker = ctx.attacker
    if attacker is None:
        return
    if not any(_is_psychic_energy(card) for card in ctx.attached_energies(attacker)):
        return
    await ctx.discard_energy_from(
        attacker, 1, predicate=_is_psychic_energy,
        prompt="Discard a Psychic Energy from Kadabra")
    await ctx.heal(ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0), attacker)


card = PokemonCardDef(
    guid="3065163c-f082-5ca1-a578-567e9396e7ad",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1", "Kadabra"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard 1 Psychic Energy card attached to Kadabra or this attack does nothing. Remove all damage counters from Kadabra.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=_can_recover,
            effect=recover,
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)