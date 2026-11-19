from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType

card = PokemonCardDef(
    guid="57eed303-2a46-56fd-b93e-76fe4698745c",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic", "Trubbish"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=568,
    abilities=[
        Attack(
            title="Pile Up",
            game_text="Flip a coin. If heads, search your deck for a Pok\u00e9mon Tool card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=flip_gate(then=search_to_hand(
                lambda card: card.get_attribute(AttrID.TRAINER_TYPE) in (
                    TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value
                ),
                count=1, reveal=True,
            )),
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)