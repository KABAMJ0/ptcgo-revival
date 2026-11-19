from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c184999-6660-544b-8842-cec40b5f902b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Superpowered Throw",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 30),
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)