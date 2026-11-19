from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_condition

card = PokemonCardDef(
    guid="82d271fc-d7e8-526e-9223-a5ca106cd779",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityVMAX.Name",
    display_name="Toxtricity VMAX",
    searchable_by=["Toxtricity VMAX", "VMAX", "ToxtricityVMAX"],
    subtypes=["VMAX"],
    collector_number=113,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityV.Name",
    family_id=849,
    abilities=[
        Attack(
            title="G-Max Riot",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=bonus_if(defender_has_condition(SpecialConditions.POISONED), 80),
        ),
    ],
)