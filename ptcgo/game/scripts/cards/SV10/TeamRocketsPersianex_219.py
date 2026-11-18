from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="3b95d677-6d4f-5c7b-8827-b5633d7ba361",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPersianex.Name",
    display_name="Team Rocket's Persian ex",
    searchable_by=["Team Rocket's Persian ex", "Stage 1", "ex", "TeamRocketsPersianex"],
    subtypes=["Stage 1", "ex"],
    collector_number=219,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMeowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Haughty Order",
            game_text="Reveal the top 10 cards of your opponent's deck. You may choose an attack from a Pok\u00e9mon you find there and use it as this attack. Shuffle the revealed cards into your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Cruel Slash",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)