from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="acc7cb63-97a4-58cc-8285-15d741954472",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekromex.Name",
    display_name="Zekrom ex",
    searchable_by=["Zekrom ex", "Basic", "ex", "Zekromex"],
    subtypes=["Basic", "ex"],
    collector_number=158,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Voltage Burst",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken. This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)