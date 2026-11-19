from ptcgo.game.card_effects.support_common import cure_conditions_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b699d00-6d5e-5ef3-95b5-91297e273619",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name",
    display_name="Gardevoir ex",
    searchable_by=["Gardevoir ex", "Stage 2", "ex", "Gardevoirex"],
    subtypes=["Stage 2", "ex"],
    collector_number=86,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psychic Embrace",
            game_text="As often as you like during your turn, you may attach a Basic Psychic Energy card from your discard pile to 1 of your Psychic Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, put 2 damage counters on that Pok\u00e9mon. You can't use this Ability on a Pok\u00e9mon that would be Knocked Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Miracle Force",
            game_text="This Pok\u00e9mon recovers from all Special Conditions.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=cure_conditions_effect("active"),
        ),
    ],
)