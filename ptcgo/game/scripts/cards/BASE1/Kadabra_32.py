from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def recover(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.PSYCHIC.value),
        prompt="Discard 1 PSYCHIC Energy card attached to Kadabra")
    if not discarded:
        return
    pokemon = ctx.attacker
    missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
    if missing > 0:
        await ctx.heal(missing, pokemon)


card = PokemonCardDef(
    guid="13e17998-12f1-5163-9d6b-b1ae6d2ea9fa",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1", "Kadabra"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="BASE1",
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
            game_text="Discard 1 Psychic Energy card attached to Kadabra in order to use this attack. Remove all damage counters from Kadabra.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=recover,
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)