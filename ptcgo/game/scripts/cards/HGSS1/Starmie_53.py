from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _cosmic_cyclone(ctx):
    waters = [energy for pokemon in ctx.my_pokemon_in_play()
              for energy in ctx.attached_energies(pokemon)
              if energy_provides_type(energy, PokemonTypes.WATER.value)]
    picks = []
    if waters:
        picks = await ctx.choose_cards(
            waters, len(waters), minimum=0,
            prompt="Choose as many Water Energy attached to your Pokémon as you like")
    if picks:
        await ctx.shuffle_into_deck(picks)
        await ctx.deal_damage(20 * len(picks))


card = PokemonCardDef(
    guid="507a591a-042f-5de3-960a-03c3ff043ad0",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Cosmic Cyclone",
            game_text="Choose as many Water Energy attached to your Pok\u00e9mon as you like. This attack does 20 damage times the number of Energy you chose. Shuffle those cards back into your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)