from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="91806871-4d24-5746-9ad8-86317da32444",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name",
    display_name="Alolan Marowak",
    searchable_by=["Alolan Marowak", "Stage 1", "AlolanMarowak"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.kos_suffered_last_turn(ctx.player_id) > 0, 90),
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)