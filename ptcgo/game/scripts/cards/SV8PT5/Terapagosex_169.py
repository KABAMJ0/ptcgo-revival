from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic, attacker_is_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f8993d74-4c3a-5fe4-83f9-cc4ff3e22da7",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagosex.Name",
    display_name="Terapagos ex",
    searchable_by=["Terapagos ex", "Basic", "Tera", "ex", "Terapagosex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=169,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1024,
    abilities=[
        Attack(
            title="Unified Beatdown",
            game_text="If you go second, you can't use this attack during your first turn. This attack does 30 damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Crown Opal",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic non-Colorless Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=180,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_basic(include_colorless=False)),
        ),
    ],
)