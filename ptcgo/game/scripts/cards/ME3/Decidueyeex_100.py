from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ac29fbc-7680-5618-bf96-5b3020c40125",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueyeex.Name",
    display_name="Decidueye ex",
    searchable_by=["Decidueye ex", "Stage 2", "ex", "Decidueyeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=100,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Sniper's Eye",
            game_text="If your opponent has exactly 4 cards in their hand, ignore all Colorless Energy in the costs of attacks used by this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Crushing Arrow",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=240,
            effect=discard_opponent_energy_attack(1),
        ),
    ],
)