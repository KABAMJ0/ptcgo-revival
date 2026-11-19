from ptcgo.game.card_effects.passives_common import flip_protection
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a575791f-c82d-5e30-8169-bfee8b0faa72",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon",
    searchable_by=["Shelgon", "Stage 1", "Shelgon"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Scrunch",
            game_text="Flip a coin. If heads, prevent all damage done to Shelgon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Dragon Bump",
            game_text="If Shelgon has any basic Fire Energy and any basic Water Energy attached to it, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)