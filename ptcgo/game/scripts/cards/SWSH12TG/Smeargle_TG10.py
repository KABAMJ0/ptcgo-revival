from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import look_top_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card

colorful_palette = look_top_attach_energy(
    5, predicate=is_basic_energy_card, rest="shuffle", distribute=False, minimum=0
)

card = PokemonCardDef(
    guid="e122ca97-b69b-59e3-9092-495cd888dfa4",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SWSH12TG",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Colorful Palette",
            game_text="Look at the top 5 cards of your deck. You may attach any number of basic Energy cards you find there to 1 of your Pok\u00e9mon. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=colorful_palette,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)