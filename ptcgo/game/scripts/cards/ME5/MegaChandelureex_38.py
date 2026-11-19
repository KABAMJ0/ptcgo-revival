from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11637729-6873-5d82-b221-7441bbd6da92",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaChandelureex.Name",
    display_name="Mega Chandelure ex",
    searchable_by=["Mega Chandelure ex", "Stage 2", "MEGA", "ex", "MegaChandelureex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=38,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Binding Flame",
            game_text="Your opponent's Active Pok\u00e9mon's Retreat Cost is Colorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Phantom Maze",
            game_text="This attack does 50 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            damage_operator="+",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 50),
        ),
    ],
)