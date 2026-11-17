from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a24b185d-f729-50bc-96f7-52c5705c42f7",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesRibombee.Name",
    display_name="Lillie's Ribombee",
    searchable_by=["Lillie's Ribombee", "Stage 1", "LilliesRibombee"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    family_id=742,
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