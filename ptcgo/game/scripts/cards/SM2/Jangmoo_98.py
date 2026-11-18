from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d78d62ac-9aa9-5f7c-b13d-0350a5685cba",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    display_name="Jangmo-o",
    searchable_by=["Jangmo-o", "Basic", "Jangmoo"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=782,
    abilities=[
        Ability(
            title="Bulletproof",
            game_text="This Pok\u00e9mon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)