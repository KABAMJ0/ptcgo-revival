from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="de86a854-bde3-562b-89c0-f86b3d7abdaa",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee", "Basic", "Combee"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=415,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={},
            effect=draw_attack(1),
        ),
        Attack(
            title="Shoot Through",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=snipe_attack(10, pool="bench", apply_modifiers=False),
        ),
    ],
)