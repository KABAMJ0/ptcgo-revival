from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import opponent_retreat_tax_passive
from ptcgo.game.card_effects.attacks_common import damage_per, defender_retreat_cost

card = PokemonCardDef(
    guid="16a8c30e-dcd4-5a59-8c9f-945ed59f8b8d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spidopsex.Name",
    display_name="Spidops ex",
    searchable_by=["Spidops ex", "Stage 1", "ex", "Spidopsex"],
    subtypes=["Stage 1", "ex"],
    collector_number=243,
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
            effect=damage_per(defender_retreat_cost, 30, base=90),
        ),
    ],
)