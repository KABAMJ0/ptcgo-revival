from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="4a797be3-d001-51a6-bae7-2601b2313280",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaurex.Name",
    display_name="Venusaur ex",
    searchable_by=["Venusaur ex", "Stage 2", "ex", "Venusaurex"],
    subtypes=["Stage 2", "ex"],
    collector_number=198,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Tranquil Flower",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may heal 60 damage from 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dangerous Toxwhip",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)