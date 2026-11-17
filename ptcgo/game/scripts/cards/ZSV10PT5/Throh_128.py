from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9ddfafd-c6c5-5032-bef5-dfce1efc8080",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic", "Throh"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Shoulder Throw",
            game_text="This attack does 30 less damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)