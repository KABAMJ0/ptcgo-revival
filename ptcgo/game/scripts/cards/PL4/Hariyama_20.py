from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b0ba9172-27e1-5395-ba9c-a344aaea34e5",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Attack(
            title="Push Out",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Vortex Chop",
            game_text="If the Defending Pok\u00e9mon has any Resistance, this attack's base damage is 120 instead of 60.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)