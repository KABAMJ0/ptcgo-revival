from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.attacks_common import count_hand, damage_per
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da79aaef-e43e-59ff-b6a3-39eb2797b5d2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1", "Ambipom"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Hand Fling",
            game_text="This attack does 20 damage for each card in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_hand("mine"), 20),
        ),
    ],
)