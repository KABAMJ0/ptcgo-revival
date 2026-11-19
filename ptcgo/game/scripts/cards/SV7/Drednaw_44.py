from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2cbcc09f-886e-5a80-a406-36235caddcc9",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drednaw.Name",
    display_name="Drednaw",
    searchable_by=["Drednaw", "Stage 1", "Drednaw"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    family_id=833,
    abilities=[
        Ability(
            title="Impervious Shell",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon if that damage is 200 or more.",
            effect=unimplemented,
        ),
        Attack(
            title="Hard Crunch",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: damage_counters_on("defender")(ctx) > 0, 80),
        ),
    ],
)