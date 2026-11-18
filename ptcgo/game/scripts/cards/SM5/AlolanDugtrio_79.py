from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.card_effects.trainers import basic_energy_of

card = PokemonCardDef(
    guid="5d5fad42-62dc-5759-80f5-7e35ef694438",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1", "AlolanDugtrio"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Gold Rush",
            game_text="Discard any number of Metal Energy cards from your hand. This attack does 30 damage for each card you discarded in this way.",
            cost={},
            damage=30,
            damage_operator="x",
            effect=discard_for_bonus(predicate=basic_energy_of("metal"), max_count=99, per=30, base=0),
        ),
    ],
)