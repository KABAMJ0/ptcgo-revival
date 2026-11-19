from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="b05385bd-ddd7-5f87-a7e6-566010c7117c",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidokingex.Name",
    display_name="Team Rocket's Nidoking ex",
    searchable_by=["Team Rocket's Nidoking ex", "Stage 2", "ex", "TeamRocketsNidokingex"],
    subtypes=["Stage 2", "ex"],
    collector_number=233,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Tainted Horn",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 8 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=condition_attack(SpecialConditions.POISONED, counters=8),
        ),
        Attack(
            title="Kingly Impact",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)