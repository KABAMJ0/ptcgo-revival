from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="24280bff-60bd-5078-b92b-f95fcf149b65",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesRibombee.Name",
    display_name="Lillie's Ribombee",
    searchable_by=["Lillie's Ribombee", "Stage 1", "LilliesRibombee"],
    subtypes=["Stage 1"],
    collector_number=183,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    family_id=743,
    abilities=[
        Ability(
            title="Inviting Wink",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have your opponent reveal their hand and you put any number of Basic Pok\u00e9mon you find there onto their Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
        ),
    ],
)