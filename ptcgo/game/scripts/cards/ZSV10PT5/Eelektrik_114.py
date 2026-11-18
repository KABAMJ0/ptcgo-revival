from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="093dc0d9-12c6-5a00-86ad-b91d3af2d1a7",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=602,
    abilities=[
        Ability(
            title="Dynamotor",
            game_text="Once during your turn, you may attach a Basic Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)