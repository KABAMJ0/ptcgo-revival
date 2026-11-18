from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack

card = PokemonCardDef(
    guid="e97fb396-ae72-5f7e-8f08-8458efe105de",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZeraoraex.Name",
    display_name="Mega Zeraora ex",
    searchable_by=["Mega Zeraora ex", "Basic", "MEGA", "ex", "MegaZeraoraex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=98,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Thunderous Fist",
            game_text="This attack does 60 damage for each Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Zepto Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=switch_self_attack(),
        ),
    ],
)