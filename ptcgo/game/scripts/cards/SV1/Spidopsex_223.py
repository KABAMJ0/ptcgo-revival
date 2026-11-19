from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import opponent_retreat_tax_passive

card = PokemonCardDef(
    guid="dc0e5ea0-d85e-5cd2-8029-c750e4b3b6d6",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spidopsex.Name",
    display_name="Spidops ex",
    searchable_by=["Spidops ex", "Stage 1", "ex", "Spidopsex"],
    subtypes=["Stage 1", "ex"],
    collector_number=223,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    family_id=917,
    abilities=[
        Ability(
            title="Trap Territory",
            game_text="Your opponent's Active Pok\u00e9mon's Retreat Cost is Colorless more.",
            passive=opponent_retreat_tax_passive(1, active_only=True),
        ),
        Attack(
            title="Wire Hang",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 30, base=90),
        ),
    ],
)