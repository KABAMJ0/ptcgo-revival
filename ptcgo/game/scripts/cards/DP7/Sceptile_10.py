from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="669e91c1-0b1c-592f-a160-34afe3b1fbaa",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="DP7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Energy Trans",
            game_text="As often as you like during your turn (before your attack), move a Grass Energy card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Sceptile is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Leaf",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Slice Drain",
            game_text="Remove 2 damage counters from Sceptile.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)