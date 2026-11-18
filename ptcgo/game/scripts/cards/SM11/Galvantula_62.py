from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="feb0651d-3b31-501e-ac1d-165a0739d174",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Live Wire",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. Also apply Weakness and Resistance for Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=True),
        ),
    ],
)