from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.pokemon import in_active_spot
from ptcgo.game.card_effects.trainers import search_to_top
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="c9ea48b2-0d14-53a3-8495-11e638f8d67a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=93,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Nighttime Maneuvers",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may use this Ability. Search your deck for a card. Shuffle your deck, then put that card on top of it.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=search_to_top(1),
        ),
        Attack(
            title="Poison Sound Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=80,
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)