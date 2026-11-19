from ptcgo.game.card_effects.attacks_common import active_is, bonus_if, has_tool
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, active_is, has_tool
card = PokemonCardDef(
    guid="de2763e5-ea51-5755-bd30-90c160ee5aee",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=182,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Assault Laser",
            game_text="If your opponent's Active Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(active_is(has_tool), 80),
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)