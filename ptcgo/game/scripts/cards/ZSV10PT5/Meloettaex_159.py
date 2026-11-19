from ptcgo.game.card_effects.passives_common import boost_own_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f5bc4bc7-a666-5238-8ada-a4aefe8554b8",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloettaex.Name",
    display_name="Meloetta ex",
    searchable_by=["Meloetta ex", "Basic", "ex", "Meloettaex"],
    subtypes=["Basic", "ex"],
    collector_number=159,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=648,
    abilities=[
        Ability(
            title="Debut Performance",
            game_text="If you go first, this Pok\u00e9mon can use attacks during your first turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=boost_own_next_turn(80, attack_title="Echoed Voice"),
        ),
    ],
)