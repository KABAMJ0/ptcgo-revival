from ptcgo.game.card_effects.passives_common import flip_prevent_damage_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5739999-bdd8-5bc6-80c2-68e59615c753",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name",
    display_name="Dragapult",
    searchable_by=["Dragapult", "Stage 2", "Dragapult"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Ability(
            title="Infiltrator",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive("Infiltrator"),
        ),
        Attack(
            title="Phantom Force",
            game_text="Put 3 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
