from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, defender_retreat_cost

card = PokemonCardDef(
    guid="f5a22eb7-e912-57bb-bf9b-1c19e370f054",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Ability(
            title="Big Net",
            game_text="Your opponent's Active Evolution Pok\u00e9mon's Retreat Cost is Colorless more.",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 30),
        ),
        Attack(
            title="String Bind",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(defender_retreat_cost, 30, base=10),
        ),
    ],
)