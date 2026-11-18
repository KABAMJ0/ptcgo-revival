from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="e44110a8-e287-575f-b7e1-a57d9a1aa7a5",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGolisopodex.Name",
    display_name="Mega Golisopod ex",
    searchable_by=["Mega Golisopod ex", "Stage 1", "MEGA", "ex", "MegaGolisopodex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=11,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Finishing Blow",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 160 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Quadruple Hold",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=no_retreat_attack(),
        ),
    ],
)