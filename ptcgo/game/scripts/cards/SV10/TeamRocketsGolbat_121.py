from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack, place_counters

card = PokemonCardDef(
    guid="207c105a-0e42-51b7-855f-0b15a633ab7d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    display_name="Team Rocket's Golbat",
    searchable_by=["Team Rocket's Golbat", "Stage 1", "TeamRocketsGolbat"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsZubat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Sneaky Bite",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=place_counters(2, target="choose_any_opponent"),
        ),
        Attack(
            title="Confuse Ray",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)