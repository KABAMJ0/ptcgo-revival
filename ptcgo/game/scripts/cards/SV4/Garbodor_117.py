from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.card_effects.trainers import is_tool_card

card = PokemonCardDef(
    guid="dd50ae07-ecda-5204-a8db-2cd2c277aad2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Attack(
            title="Chuck",
            game_text="Discard any number of Pok\u00e9mon Tool cards from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=50,
            damage_operator="x",
            effect=discard_for_bonus(predicate=is_tool_card, max_count=99, per=50, base=0),
        ),
        Attack(
            title="Venomous Hit",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)