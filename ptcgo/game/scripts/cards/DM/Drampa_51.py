from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _is_dragon_pokemon(pokemon):
    return PokemonTypes.DRAGON.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def dragon_wisdom(ctx):
    """The printed 20 is dealt by attach_from_discard, which then attaches a
    basic Energy from the discard pile to 1 of your Dragon Pokemon."""
    await attach_from_discard(is_basic_energy_card, count=1, target=_is_dragon_pokemon,
                              prompt="Choose a basic Energy from your discard pile")(ctx)

card = PokemonCardDef(
    guid="bc682941-5896-5c07-a4ec-2f6e5772e2c4",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=780,
    abilities=[
        Attack(
            title="Dragon Wisdom",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Dragon Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=dragon_wisdom,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)