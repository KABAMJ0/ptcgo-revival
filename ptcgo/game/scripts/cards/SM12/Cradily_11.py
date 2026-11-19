from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import condition_retreat_lock_passive
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="0f280013-bd05-549c-b845-877b55dcd80a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 2", "Cradily"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Ability(
            title="Swaying Strangle",
            game_text="Your opponent's Pok\u00e9mon that are affected by Special Conditions can't retreat.",
            passive=condition_retreat_lock_passive(conditions="any"),
        ),
        Attack(
            title="Poison Tentacles",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)