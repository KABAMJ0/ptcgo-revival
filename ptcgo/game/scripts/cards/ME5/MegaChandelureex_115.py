from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import opponent_retreat_tax_passive


card = PokemonCardDef(
    guid="b41160a3-c95c-5b68-a982-7cfabf6d265d",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaChandelureex.Name",
    display_name="Mega Chandelure ex",
    searchable_by=["Mega Chandelure ex", "MEGA", "ex", "MegaChandelureex"],
    subtypes=["MEGA", "ex"],
    collector_number=115,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Binding Flame",
            game_text="Your opponent's Active Pok\u00e9mon's Retreat Cost is Colorless more.",
            passive=opponent_retreat_tax_passive(1, active_only=True),
        ),
        Attack(
            title="Phantom Maze",
            game_text="This attack does 50 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            damage_operator="+",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 50, base=130),
        ),
    ],
)