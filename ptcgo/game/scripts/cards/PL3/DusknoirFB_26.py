from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9aa825c6-e88d-5648-a4e1-8d82c319b259",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DusknoirFB.Name",
    display_name="Dusknoir FB",
    searchable_by=["Dusknoir FB", "Basic", "SP", "DusknoirFB"],
    subtypes=["Basic", "SP"],
    collector_number=26,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=477,
    abilities=[
        Attack(
            title="Ghost Hand",
            game_text="Put 1 damage counter on 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Cursed Wrath",
            game_text="Does 10 damage times the number of Pok\u00e9mon SP in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)