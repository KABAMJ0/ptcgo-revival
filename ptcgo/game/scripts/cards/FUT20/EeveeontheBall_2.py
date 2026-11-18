from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c921906-b5ec-5fa4-b3a3-08e21e83f9e2",
    key="FUT20",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeontheBall.Name",
    display_name="Eevee on the Ball",
    searchable_by=["Eevee on the Ball", "Basic", "EeveeontheBall"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="FUT20",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Make the Assist",
            game_text="Attach a basic Energy card from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)