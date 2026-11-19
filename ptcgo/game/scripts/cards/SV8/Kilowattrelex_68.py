from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68ef513d-1221-5ced-919a-d44850e23ada",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrelex.Name",
    display_name="Kilowattrel ex",
    searchable_by=["Kilowattrel ex", "Stage 1", "ex", "Kilowattrelex"],
    subtypes=["Stage 1", "ex"],
    collector_number=68,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Return Charge",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, attach up to 2 Basic Lightning Energy cards from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=damage_per(count_energy("self", "lightning"), 40),
        ),
        Attack(
            title="Thunder Lance",
            game_text="This attack does 40 more damage for each Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)