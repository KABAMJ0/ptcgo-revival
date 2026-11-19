from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="d89be7f3-3c7f-57be-887b-9393bc692953",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsRattata.Name",
    display_name="Team Rocket's Rattata",
    searchable_by=["Team Rocket's Rattata", "Basic", "TeamRocketsRattata"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Attack(
            title="Dangerous Incisors",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)