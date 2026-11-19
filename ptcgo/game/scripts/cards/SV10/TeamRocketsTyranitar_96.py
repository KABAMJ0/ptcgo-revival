from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="452d4aa6-8b9c-5dd8-877e-877550c43266",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTyranitar.Name",
    display_name="Team Rocket's Tyranitar",
    searchable_by=["Team Rocket's Tyranitar", "Stage 2", "TeamRocketsTyranitar"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Sand Stream",
            game_text="During Pok\u00e9mon Checkup, if this Pok\u00e9mon is in the Active Spot, put 2 damage counters on each of your opponent's Basic Pok\u00e9mon.",
            effect=discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Demolition Tackle",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=discard_opponent_energy_attack(1),
        ),
    ],
)