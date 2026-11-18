from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="267212fc-4912-5c58-8808-7a23d877e421",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargoex.Name",
    display_name="Magcargo ex",
    searchable_by=["Magcargo ex", "Stage 1", "Tera", "ex", "Magcargoex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=191,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Hot Magma",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Ground Burn",
            game_text="Discard the top card of each player's deck. This attack does 140 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)