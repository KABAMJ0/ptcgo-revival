from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="7b7f240c-0e63-5a5d-964d-0b456ab3ef77",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianArticunoV.Name",
    display_name="Galarian Articuno V",
    searchable_by=["Galarian Articuno V", "Basic", "V", "GalarianArticunoV"],
    subtypes=["Basic", "V"],
    collector_number=16,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Reconstitute",
            game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyray",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)