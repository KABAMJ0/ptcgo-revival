from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_discard
from ptcgo.game.session.effects import is_item_card

card = PokemonCardDef(
    guid="ab4f0380-d3ac-5433-a659-7312f4effe58",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=95,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Durable Blade",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, put it into your hand instead of the discard pile. (Discard all cards attached to it.)",
            effect=unimplemented,
        ),
        Attack(
            title="Trash Slash",
            game_text="This attack does 10 damage for each Item card in your discard pile. You can't do more than 130 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_discard("mine", is_item_card), 10, cap=130),
        ),
    ],
)